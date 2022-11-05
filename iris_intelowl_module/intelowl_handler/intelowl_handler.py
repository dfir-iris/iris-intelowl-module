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
from jinja2 import Template

import iris_interface.IrisInterfaceStatus as InterfaceStatus
from app.datamgmt.manage.manage_attribute_db import add_tab_attribute_field

from pyintelowl import IntelOwl, IntelOwlClientException


class IntelowlHandler(object):
    def __init__(self, mod_config, server_config, logger):
        self.mod_config = mod_config
        self.server_config = server_config
        self.intelowl = self.get_intelowl_instance()
        self.log = logger

    def get_intelowl_instance(self):
        """
        Returns an intelowl API instance depending if the key is premium or not

        :return: IntelOwl Instance
        """
        url = self.mod_config.get('intelowl_url')
        key = self.mod_config.get('intelowl_key')
        should_use_proxy = self.mod_config.get('intelowl_should_use_proxy')
        proxies = {}

        if should_use_proxy is True:
            if self.server_config.get('http_proxy'):
                proxies['https'] = self.server_config.get('HTTPS_PROXY')

            if self.server_config.get('https_proxy'):
                proxies['http'] = self.server_config.get('HTTP_PROXY')

        intelowl = IntelOwl(
            key,
            url,
            None,
            proxies=proxies
        )

        return intelowl

    def gen_domain_report_from_template(self, html_template, intelowl_report) -> InterfaceStatus:
        """
        Generates an HTML report for Domain, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param intelowl_report: The JSON report fetched with intelowl API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = intelowl_report
        pre_render = dict({"results": []})

        for intelowl_result in context:
            pre_render["results"].append(intelowl_result)

        try:
            rendered = template.render(pre_render)

        except Exception:

            self.log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def gen_ip_report_from_template(self, html_template, intelowl_report) -> InterfaceStatus:
        """
        Generates an HTML report for IP, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param intelowl_report: The JSON report fetched with intelowl API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = intelowl_report
        pre_render = dict({"results": []})

        for intelowl_result in context:
            pre_render["results"].append(intelowl_result)

        try:
            rendered = template.render(pre_render)

        except Exception:

            self.log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def gen_url_report_from_template(self, html_template, intelowl_report) -> InterfaceStatus:
        """
        Generates an HTML report for URL, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param intelowl_report: The JSON report fetched with intelowl API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = intelowl_report
        pre_render = dict({"results": []})

        for intelowl_result in context:
            pre_render["results"].append(intelowl_result)

        try:
            rendered = template.render(pre_render)

        except Exception:

            self.log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def gen_hash_report_from_template(self, html_template, intelowl_report) -> InterfaceStatus:
        """
        Generates an HTML report for Hash, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param intelowl_report: The JSON report fetched with intelowl API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = intelowl_report
        pre_render = dict({"results": []})

        for intelowl_result in context:
            pre_render["results"].append(intelowl_result)

        try:
            rendered = template.render(pre_render)

        except Exception:

            self.log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def gen_generic_report_from_template(self, html_template, intelowl_report) -> InterfaceStatus:
        """
        Generates an HTML report for Generic ioc, displayed as an attribute in the IOC

        :param html_template: A string representing the HTML template
        :param intelowl_report: The JSON report fetched with intelowl API
        :return: InterfaceStatus
        """
        template = Template(html_template)
        context = intelowl_report
        pre_render = dict({"results": []})

        for intelowl_result in context:
            pre_render["results"].append(intelowl_result)

        try:
            rendered = template.render(pre_render)

        except Exception:

            self.log.error(traceback.format_exc())
            return InterfaceStatus.I2Error(traceback.format_exc())

        return InterfaceStatus.I2Success(data=rendered)

    def handle_domain(self, ioc):
        """
        Handles an IOC of type domain and adds IntelOwl insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting domain report for {ioc.ioc_value}')

        domain = ioc.ioc_value
        results = self.intelowl.send_observable_analysis_request(observable_name=domain, observable_classification="domain")
        job_id = results["job_id"]

        if self.mod_config.get('intelowl_report_as_attribute') is True:
            self.log.info('Adding new attribute IntelOwl Domain Report to IOC')

            report = [results]

            status = self.gen_domain_report_from_template(self.mod_config.get('intelowl_domain_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='IntelOwl Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()

    def handle_ip(self, ioc):
        """
        Handles an IOC of type ip and adds IntelOwl insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting IP report for {ioc.ioc_value}')

        ip = ioc.ioc_value
        results = self.intelowl.send_observable_analysis_request(observable_name=ip, observable_classification="ip")
        job_id = results["job_id"]

        if self.mod_config.get('intelowl_report_as_attribute') is True:
            self.log.info('Adding new attribute IntelOwl IP Report to IOC')

            report = [results]

            status = self.gen_ip_report_from_template(self.mod_config.get('intelowl_ip_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='IntelOwl Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()

    def handle_url(self, ioc):
        """
        Handles an IOC of type URL and adds IntelOwl insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting URL report for {ioc.ioc_value}')

        url = ioc.ioc_value
        results = self.intelowl.send_observable_analysis_request(observable_name=url, observable_classification="url")
        job_id = results["job_id"]

        if self.mod_config.get('intelowl_report_as_attribute') is True:
            self.log.info('Adding new attribute IntelOwl URL Report to IOC')

            report = [results]

            status = self.gen_url_report_from_template(self.mod_config.get('intelowl_url_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='IntelOwl Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()

    def handle_hash(self, ioc):
        """
        Handles an IOC of type hash and adds IntelOwl insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting hash report for {ioc.ioc_value}')

        hash = ioc.ioc_value
        results = self.intelowl.send_observable_analysis_request(observable_name=hash, observable_classification="hash")
        job_id = results["job_id"]

        if self.mod_config.get('intelowl_report_as_attribute') is True:
            self.log.info('Adding new attribute IntelOwl hash Report to IOC')

            report = [results]

            status = self.gen_hash_report_from_template(self.mod_config.get('intelowl_hash_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='IntelOwl Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()

    def handle_generic(self, ioc):
        """
        Handles an IOC of type generic and adds IntelOwl insights

        :param ioc: IOC instance
        :return: IIStatus
        """

        self.log.info(f'Getting generic report for {ioc.ioc_value}')

        generic = ioc.ioc_value
        results = self.intelowl.send_observable_analysis_request(observable_name=generic, observable_classification="generic")
        job_id = results["job_id"]

        if self.mod_config.get('intelowl_report_as_attribute') is True:
            self.log.info('Adding new attribute IntelOwl generic Report to IOC')

            report = [results]

            status = self.gen_generic_report_from_template(self.mod_config.get('intelowl_generic_report_template'), report)

            if not status.is_success():
                return status

            rendered_report = status.get_data()

            try:
                add_tab_attribute_field(ioc, tab_name='IntelOwl Report', field_name="HTML report", field_type="html",
                                        field_value=rendered_report)

            except Exception:

                self.log.error(traceback.format_exc())
                return InterfaceStatus.I2Error(traceback.format_exc())
        else:
            self.log.info('Skipped adding attribute report. Option disabled')

        return InterfaceStatus.I2Success()
