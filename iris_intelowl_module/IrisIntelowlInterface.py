#!/usr/bin/env python3
#
#
#  IRIS intelowl Source Code
#  Copyright (C) 2022 - dfir-iris
#  contact@dfir-iris.org
#  Created by dfir-iris - 2022-10-29
#
#  License Apache Software License 3.0

import traceback
from pathlib import Path

import iris_interface.IrisInterfaceStatus as InterfaceStatus
from iris_interface.IrisModuleInterface import IrisPipelineTypes, IrisModuleInterface, IrisModuleTypes

import iris_intelowl_module.IrisIntelowlConfig as interface_conf
from iris_intelowl_module.intelowl_handler.intelowl_handler import IntelowlHandler


class IrisIntelowlInterface(IrisModuleInterface):
    """
    Provide the interface between Iris and IntelowlHandler
    """
    name = "IrisIntelowlInterface"
    _module_name = interface_conf.module_name
    _module_description = interface_conf.module_description
    _interface_version = interface_conf.interface_version
    _module_version = interface_conf.module_version
    _pipeline_support = interface_conf.pipeline_support
    _pipeline_info = interface_conf.pipeline_info
    _module_configuration = interface_conf.module_configuration

    _module_type = IrisModuleTypes.module_processor

    def register_hooks(self, module_id: int):
        """
        Registers all the hooks

        :param module_id: Module ID provided by IRIS
        :return: Nothing
        """
        self.module_id = module_id
        module_conf = self.module_dict_conf
        if module_conf.get('intelowl_on_create_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_postload_ioc_create')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_postload_ioc_create hook")
        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_postload_ioc_create')

        if module_conf.get('intelowl_on_update_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_postload_ioc_update')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_postload_ioc_update hook")
        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_postload_ioc_update')

        if module_conf.get('intelowl_manual_hook_enabled'):
            status = self.register_to_hook(module_id, iris_hook_name='on_manual_trigger_ioc',
                                           manual_hook_name='Get IntelOwl insight')
            if status.is_failure():
                self.log.error(status.get_message())
                self.log.error(status.get_data())

            else:
                self.log.info("Successfully registered on_manual_trigger_ioc hook")

        else:
            self.deregister_from_hook(module_id=self.module_id, iris_hook_name='on_manual_trigger_ioc')

    def hooks_handler(self, hook_name: str, hook_ui_name: str, data: any):
        """
        Hooks handler table. Calls corresponding methods depending on the hooks name.

        :param hook_name: Name of the hook which triggered
        :param hook_ui_name: Name of the ui hook
        :param data: Data associated with the trigger.
        :return: Data
        """

        self.log.info(f'Received {hook_name}')
        if hook_name in ['on_postload_ioc_create', 'on_postload_ioc_update', 'on_manual_trigger_ioc']:
            status = self._handle_ioc(data=data)

        else:
            self.log.critical(f'Received unsupported hook {hook_name}')
            return InterfaceStatus.I2Error(data=data, logs=list(self.message_queue))

        if status.is_failure():
            self.log.error(f"Encountered error processing hook {hook_name}")
            return InterfaceStatus.I2Error(data=data, logs=list(self.message_queue))

        self.log.info(f"Successfully processed hook {hook_name}")
        return InterfaceStatus.I2Success(data=data, logs=list(self.message_queue))

    def _handle_ioc(self, data) -> InterfaceStatus.IIStatus:
        """
        Handle the IOC data the module just received. The module registered
        to on_postload hooks, so it receives instances of IOC object.
        These objects are attached to a dedicated SQlAlchemy session so data can
        be modified safely.

        :param data: Data associated to the hook, here IOC object
        :return: IIStatus
        """

        intelowl_handler = IntelowlHandler(mod_config=self.module_dict_conf,
                                           server_config=self.server_dict_conf,
                                           logger=self.log)

        in_status = InterfaceStatus.IIStatus(code=InterfaceStatus.I2CodeNoError)

        for element in data:
            # Check that the IOC we receive is of type the module can handle and dispatch
            if 'ip-' in element.ioc_type.type_name:
                status = intelowl_handler.handle_ip(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)
            elif 'domain' in element.ioc_type.type_name:
                status = intelowl_handler.handle_domain(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)
            elif 'url' in element.ioc_type.type_name:
                status = intelowl_handler.handle_url(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)
            elif element.ioc_type.type_name in ['md5', 'sha1', 'sha224', 'sha256', 'sha512']:
                status = intelowl_handler.handle_hash(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)
            else:
                status = intelowl_handler.handle_generic(ioc=element)
                in_status = InterfaceStatus.merge_status(in_status, status)

            # elif element.ioc_type.type_name in etc...

            #else:
            #    self.log.error(f'IOC type {element.ioc_type.type_name} not handled by intelowl module. Skipping')

        return in_status(data=data)
