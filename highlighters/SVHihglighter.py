"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       SVHighlighter.py
Description:     

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

from highlighters.highLighter import Highlighter
import re
import tkinter as tk


class SVHighlighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.keyword_tag = "keyword"
        self.type_tag = "type"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.number_tag = "number"
        self.uvm_class_tag = "uvm_class"
        self.uvm_macro_tag = "uvm_macro"
        
        self.keywords = ["rtranif0", "begin", "always", "ifnone", "rpmos", "and", "initial", "rtran", "assign",
                         "rtranif1", "buf", "bufif0", "join", "small", "bufif1", "large", "specify", "case",
                         "macromodule", "specparam", "casex", "medium", "strong0", "casez", "module", "strong1", "cmos",
                         "nand", "deassign", "negedge", "default", "nmos", "table", "defparam", "nor", "task",
                         "disable", "not", "edge", "notif0", "tran", "else", "notif1", "tranif0", "end", "or",
                         "tranif1", "endcase", "endmodule", "endprimitive", "posedge", "endspecify", "primitive",
                         "endfunction", "pmos", "endtable", "pull0", "endtask", "pull1", "pullup", "wait", "for",
                         "pulldown", "while", "function", "weak1", "fork", "force", "rcmos", "weak0", "forever",
                         "highz0", "release", "highz1", "repeat", "xnor", "if", "rnmos", "xor", "return", "super",
                         "new", "package", "endpackage", "class", "extends", "endclass", "this", "enum", "virtual"]

        self.types = ["input", "inout", "integer", "scalared", "supply0", "supply1", "time", "output", "tri",
                      "parameter", "tri0", "tri1", "triand", "trior", "trireg", "vectored", "event", "wand", "real",
                      "realtime", "reg", "wire", "wor", "int", "string", "logic"]

        self.uvm_classes = [
            "uvm_object", "uvm_component", "uvm_env", "uvm_agent", "uvm_sequencer_base", "uvm_driver",
            "uvm_sequence_item", "uvm_sequence", "uvm_sequence_library", "uvm_subscriber", "uvm_monitor",
            "uvm_scoreboard", "uvm_push_driver", "uvm_pull_sequencer", "uvm_reg", "uvm_reg_field", "uvm_reg_block",
            "uvm_reg_adapter", "uvm_reg_predictor", "uvm_reg_frontdoor", "uvm_reg_backdoor", "uvm_tlm_fifo",
            "uvm_analysis_export", "uvm_analysis_imp", "uvm_analysis_port", "uvm_sequencer_param_base", "uvm_event",
            "uvm_barrier", "uvm_barrier_cb", "uvm_tlm_fifo_base", "uvm_tlm_analysis_fifo", "uvm_mem", "uvm_mem_region",
            "uvm_mem_ral_block", "uvm_mem_ral", "uvm_mem_ral_seq", "uvm_resource_db", "uvm_config_db",
            "uvm_coreservice_t", "uvm_default_coreservice_t", "uvm_driver_cbs", "uvm_reg_cbs", "uvm_report_catcher",
            "uvm_root", "uvm_tlm_fifo_size_if", "uvm_cmdline_processor", "uvm_cmdline_options", "uvm_event_pool",
            "uvm_timeout", "uvm_merger"
        ]
        self.uvm_macros = [
            "uvm_component_utils", "uvm_component_utils_param", "uvm_component_utils_begin",
            "uvm_component_utils_end", "uvm_object_utils", "uvm_object_param_utils", "uvm_object_registry",
            "uvm_factory_override", "uvm_default_factory", "uvm_sequence_library", "uvm_sequence_utils",
            "uvm_sequence_library_defines", "uvm_info", "uvm_warning", "uvm_error", "uvm_fatal",
            "uvm_report_info", "uvm_report_warning", "uvm_report_error", "uvm_report_fatal",
            "uvm_info_context",
            "uvm_error_context", "uvm_warning_context", "uvm_fatal_context", "uvm_config_db",
            "uvm_verbosity",
            "uvm_object_utils_copy", "uvm_object_utils_clone", "uvm_object_utils_clone_type",
            "uvm_object_utils_copy_with", "uvm_object_utils_deep_copy", "uvm_object_utils_deep_copy_with",
            "uvm_object_utils_deep_compare", "uvm_field_int", "uvm_field_string", "uvm_field_bit",
            "uvm_field_byte", "uvm_field_enum", "uvm_field_real", "uvm_field_time", "uvm_field_longint",
            "uvm_field_array_int", "uvm_field_array_string", "uvm_field_array_bit", "uvm_field_array_byte",
            "uvm_field_array_enum", "uvm_field_array_real", "uvm_field_array_time",
            "uvm_field_array_longint", "uvm_field_object", "uvm_field_object_utils",
            "uvm_field_object_utils_array",
            "uvm_field_object_utils_s", "uvm_field_object_utils_sa", "uvm_field_object_utils_v",
            "uvm_field_object_utils_vs", "uvm_cmdline_processor", "uvm_global_context", "uvm_field_declare",
            "uvm_void", "uvm_which_packer", "uvm_component_registry", "uvm_analysis_imp_decl"
        ]


    """
    
    """
    def highlight_keywords(self):
        self.text_widget.tag_remove(self.keyword_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.keywords:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.keyword_tag, start, end)
                self.text_widget.tag_configure(self.keyword_tag, foreground="orange")


    """
    
    """
    def highlight_types(self):
        self.text_widget.tag_remove(self.type_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.types:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.type_tag, start, end)
                self.text_widget.tag_configure(self.type_tag, foreground="#77d197")


    """
    
    """
    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'/\*.*?\*/', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")

        matches = re.finditer(r'//.*?\n', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")


    """
    
    """
    def highlight_strings(self):
        self.text_widget.tag_remove(self.string_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'".*?"', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")


    """
    
    """
    def highlight_uvm_classes(self):
        self.text_widget.tag_remove(self.uvm_class_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.uvm_classes:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.uvm_class_tag, start, end)
                self.text_widget.tag_configure(self.uvm_class_tag, foreground="#ffff66")


    """
    
    """
    def highlight_uvm_macros(self):
        self.text_widget.tag_remove(self.uvm_macro_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.uvm_macros:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                if start_pos > 0:
                    start_pos -= 1
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.uvm_macro_tag, start, end)
                self.text_widget.tag_configure(self.uvm_macro_tag, foreground="#c0c0c0")


    def highlight_numbers(self):
        self.text_widget.tag_remove(self.number_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'\b\d+\b', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.number_tag, start, end)
            self.text_widget.tag_configure(self.number_tag, foreground="#d31a38")

    """
    
    """
    def highlight(self):
        self.highlight_keywords()
        self.highlight_types()
        self.highlight_uvm_classes()
        self.highlight_uvm_macros()
        self.highlight_strings()
        self.highlight_comments()
        self.highlight_numbers()

