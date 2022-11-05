#!/usr/bin/env python3
#
#
#  IRIS intelowl Source Code
#  Copyright (C) 2022 - dfir-iris
#  contact@dfir-iris.org
#  Created by dfir-iris - 2022-10-29
#
#  License Apache Software License 3.0

module_name = "IrisIntelowl"
module_description = ""
interface_version = 1.1
module_version = 1.0

pipeline_support = False
pipeline_info = {}


module_configuration = [
    {
        "param_name": "intelowl_url",
        "param_human_name": "IntelOwl URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "intelowl_key",
        "param_human_name": "IntelOwl API key",
        "param_description": "IntelOwl API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    },
    {
        "param_name": "intelowl_should_use_proxy",
        "param_human_name": "Set global proxy settings for IntelOwl module",
        "param_description": "Set true or false to decide whether or not the global proxy settings should be set for "
                             "IntelOwl usage",
        "default": False,
        "mandatory": True,
        "type": "bool"
    },
    {
        "param_name": "intelowl_manual_hook_enabled",
        "param_human_name": "Manual triggers on IOCs",
        "param_description": "Set to True to offers possibility to manually triggers the module via the UI",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "intelowl_on_create_hook_enabled",
        "param_human_name": "Triggers automatically on IOC create",
        "param_description": "Set to True to automatically add a IntelOwl insight each time an IOC is created",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "intelowl_on_update_hook_enabled",
        "param_human_name": "Triggers automatically on IOC update",
        "param_description": "Set to True to automatically add a IntelOwl insight each time an IOC is updated",
        "default": False,
        "mandatory": True,
        "type": "bool",
        "section": "Triggers"
    },
    {
        "param_name": "intelowl_report_as_attribute",
        "param_human_name": "Add IntelOwl report as new IOC attribute",
        "param_description": "Creates a new attribute on the IOC, base on the IntelOwl report. Attributes are based "
                             "on the templates of this configuration",
        "default": True,
        "mandatory": True,
        "type": "bool",
        "section": "Insights"
    },
    {
        "param_name": "intelowl_domain_report_template",
        "param_human_name": "Domain report template",
        "param_description": "Domain report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>intelowl raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_intelowl\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_intelowl\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_intelowl\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        intelowl raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_intelowl\" class=\"collapse\" aria-labelledby=\"drop_r_intelowl\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='intelowl_raw_ace'>{{ results| tojson(indent=4) }}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar intelowl_in_raw = ace.edit("
                   "\"intelowl_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nintelowl_in_raw.setReadOnly(true);\nintelowl_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nintelowl_in_raw.session.setMode("
                   "\"ace/mode/json\");\nintelowl_in_raw.renderer.setShowGutter("
                   "true);\nintelowl_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nintelowl_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nintelowl_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nintelowl_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nintelowl_in_raw.session.setUseWrapMode("
                   "true);\nintelowl_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nintelowl_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    },
    {
        "param_name": "intelowl_ip_report_template",
        "param_human_name": "IP report template",
        "param_description": "IP report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>intelowl raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_intelowl\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_intelowl\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_intelowl\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        intelowl raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_intelowl\" class=\"collapse\" aria-labelledby=\"drop_r_intelowl\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='intelowl_raw_ace'>{{ results| tojson(indent=4) }}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar intelowl_in_raw = ace.edit("
                   "\"intelowl_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nintelowl_in_raw.setReadOnly(true);\nintelowl_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nintelowl_in_raw.session.setMode("
                   "\"ace/mode/json\");\nintelowl_in_raw.renderer.setShowGutter("
                   "true);\nintelowl_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nintelowl_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nintelowl_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nintelowl_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nintelowl_in_raw.session.setUseWrapMode("
                   "true);\nintelowl_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nintelowl_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    },
    {
        "param_name": "intelowl_url_report_template",
        "param_human_name": "URL report template",
        "param_description": "URL report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>intelowl raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_intelowl\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_intelowl\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_intelowl\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        intelowl raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_intelowl\" class=\"collapse\" aria-labelledby=\"drop_r_intelowl\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='intelowl_raw_ace'>{{ results| tojson(indent=4) }}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar intelowl_in_raw = ace.edit("
                   "\"intelowl_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nintelowl_in_raw.setReadOnly(true);\nintelowl_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nintelowl_in_raw.session.setMode("
                   "\"ace/mode/json\");\nintelowl_in_raw.renderer.setShowGutter("
                   "true);\nintelowl_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nintelowl_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nintelowl_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nintelowl_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nintelowl_in_raw.session.setUseWrapMode("
                   "true);\nintelowl_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nintelowl_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    },
    {
        "param_name": "intelowl_hash_report_template",
        "param_human_name": "Hash report template",
        "param_description": "Hash report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>intelowl raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_intelowl\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_intelowl\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_intelowl\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        intelowl raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_intelowl\" class=\"collapse\" aria-labelledby=\"drop_r_intelowl\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='intelowl_raw_ace'>{{ results| tojson(indent=4) }}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar intelowl_in_raw = ace.edit("
                   "\"intelowl_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nintelowl_in_raw.setReadOnly(true);\nintelowl_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nintelowl_in_raw.session.setMode("
                   "\"ace/mode/json\");\nintelowl_in_raw.renderer.setShowGutter("
                   "true);\nintelowl_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nintelowl_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nintelowl_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nintelowl_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nintelowl_in_raw.session.setUseWrapMode("
                   "true);\nintelowl_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nintelowl_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    },
    {
        "param_name": "intelowl_generic_report_template",
        "param_human_name": "Generic ioc report template",
        "param_description": "Generic ioc report template used to add a new custom attribute to the target IOC",
        "default": "<div class=\"row\">\n    <div class=\"col-12\">\n        <div "
                   "class=\"accordion\">\n            <h3>intelowl raw results</h3>\n\n           "
                   " <div class=\"card\">\n                <div class=\"card-header "
                   "collapsed\" id=\"drop_r_intelowl\" data-toggle=\"collapse\" "
                   "data-target=\"#drop_raw_intelowl\" aria-expanded=\"false\" "
                   "aria-controls=\"drop_raw_intelowl\" role=\"button\">\n                    <div "
                   "class=\"span-icon\">\n                        <div "
                   "class=\"flaticon-file\"></div>\n                    </div>\n              "
                   "      <div class=\"span-title\">\n                        intelowl raw "
                   "results\n                    </div>\n                    <div "
                   "class=\"span-mode\"></div>\n                </div>\n                <div "
                   "id=\"drop_raw_intelowl\" class=\"collapse\" aria-labelledby=\"drop_r_intelowl\" "
                   "style=\"\">\n                    <div class=\"card-body\">\n              "
                   "          <div id='intelowl_raw_ace'>{{ results| tojson(indent=4) }}</div>\n  "
                   "                  </div>\n                </div>\n            </div>\n    "
                   "    </div>\n    </div>\n</div> \n<script>\nvar intelowl_in_raw = ace.edit("
                   "\"intelowl_raw_ace\",\n{\n    autoScrollEditorIntoView: true,\n    minLines: "
                   "30,\n});\nintelowl_in_raw.setReadOnly(true);\nintelowl_in_raw.setTheme("
                   "\"ace/theme/tomorrow\");\nintelowl_in_raw.session.setMode("
                   "\"ace/mode/json\");\nintelowl_in_raw.renderer.setShowGutter("
                   "true);\nintelowl_in_raw.setOption(\"showLineNumbers\", "
                   "true);\nintelowl_in_raw.setOption(\"showPrintMargin\", "
                   "false);\nintelowl_in_raw.setOption(\"displayIndentGuides\", "
                   "true);\nintelowl_in_raw.setOption(\"maxLines\", "
                   "\"Infinity\");\nintelowl_in_raw.session.setUseWrapMode("
                   "true);\nintelowl_in_raw.setOption(\"indentedSoftWrap\", "
                   "true);\nintelowl_in_raw.renderer.setScrollMargin(8, 5);\n</script> ",
        "mandatory": False,
        "type": "textfield_html",
        "section": "Templates"
    }
    
]