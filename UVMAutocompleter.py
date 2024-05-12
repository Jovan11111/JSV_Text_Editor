import tkinter as tk
import re


class UVMAutocompleter(tk.Text):
    def __init__(self, *args, **kwargs):
        self._uvm_classes = kwargs.pop("uvm_classes", [])
        self._uvm_macros = kwargs.pop("uvm_macros", [])
        super().__init__(*args, **kwargs)

        self.bind("<Any-KeyRelease>", self._autocomplete)

    def _autocomplete(self, event):
        if event.char:
            word = self.get_word_under_cursor()

            matches = self.get_matches(word)

            if matches:
                remainder = matches[0][len(word):]

                insert = self.index("insert")
                self.insert(insert, remainder, ("sel", "autocomplete"))

                self.mark_set("insert", f"{insert}+{len(remainder)}c")

    def get_word_under_cursor(self):
        cursor_index = self.index(tk.INSERT)

        line_text = self.get(f"{cursor_index.split('.')[0]}.0", cursor_index)
        match = re.search(r'\b\w+$|`[^\s`]+$', line_text)

        return match.group() if match else ""

    def get_matches(self, word):
        matches = []
        print(word)
        if word.startswith("uvm_"):
            matches.extend([x for x in self._uvm_classes if x.startswith(word)])
        if word.startswith("`uvm_"):
            matches.extend([x for x in self._uvm_macros if x.startswith(word)])
        return matches


uvm_classes = [
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

uvm_macros = [
    "`uvm_component_utils()", "`uvm_component_utils_param()", "`uvm_component_utils_begin()",
    "`uvm_component_utils_end()", "`uvm_object_utils()", "`uvm_object_param_utils()", "`uvm_object_registry()",
    "`uvm_factory_override()", "`uvm_default_factory()", "`uvm_sequence_library()", "`uvm_sequence_utils()",
    "`uvm_sequence_library_defines()", "`uvm_info()", "`uvm_warning()", "`uvm_error()", "`uvm_fatal()",
    "`uvm_report_info()", "`uvm_report_warning()", "`uvm_report_error()", "`uvm_report_fatal()", "`uvm_info_context()",
    "`uvm_error_context()", "`uvm_warning_context()", "`uvm_fatal_context()", "`uvm_config_db()", "`uvm_verbosity()",
    "`uvm_object_utils_copy()", "`uvm_object_utils_clone()", "`uvm_object_utils_clone_type()",
    "`uvm_object_utils_copy_with()", "`uvm_object_utils_deep_copy()", "`uvm_object_utils_deep_copy_with()",
    "`uvm_object_utils_deep_compare()", "`uvm_field_int()", "`uvm_field_string()", "`uvm_field_bit()",
    "`uvm_field_byte()", "`uvm_field_enum()", "`uvm_field_real()", "`uvm_field_time()", "`uvm_field_longint",
    "`uvm_field_array_int()", "`uvm_field_array_string()", "`uvm_field_array_bit()", "`uvm_field_array_byte()",
    "`uvm_field_array_enum()", "`uvm_field_array_real()", "`uvm_field_array_time()",
    "`uvm_field_array_longint()", "`uvm_field_object()", "`uvm_field_object_utils()", "`uvm_field_object_utils_array()",
    "`uvm_field_object_utils_s()", "`uvm_field_object_utils_sa()", "`uvm_field_object_utils_v()",
    "`uvm_field_object_utils_vs()", "`uvm_cmdline_processor()", "`uvm_global_context()", "`uvm_field_declare()",
    "`uvm_void()", "`uvm_which_packer()", "`uvm_component_registry()"
]

