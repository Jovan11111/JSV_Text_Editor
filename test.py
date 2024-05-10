import tkinter as tk

class UVMAutocompleter(tk.Text):
    def __init__(self, *args, **kwargs):
        self._uvm_classes = kwargs.pop("uvm_classes", [])
        super().__init__(*args, **kwargs)

        # bind on key release, which will happen after tkinter
        # inserts the typed character
        self.bind("<Any-KeyRelease>", self._autocomplete)

        # special handling for tab, which needs to happen on the
        # key _press_
        self.bind("<Tab>", self._handle_tab)

    def _handle_tab(self, event):
        # see if any text has the "autocomplete" tag
        tag_ranges= self.tag_ranges("autocomplete")
        if tag_ranges:
            # move the insertion cursor to the end of
            # the selected text, and then remove the "sel"
            # and "autocomplete" tags
            self.mark_set("insert", tag_ranges[1])
            self.tag_remove("sel", "1.0", "end")
            self.tag_remove("autocomplete", "1.0", "end")

            # prevent the default behavior of inserting a literal tab
            return "break"

    def _autocomplete(self, event):
        if event.char:
            # get word preceeding the insertion cursor
            word = self.get("insert-1c wordstart", "insert-1c wordend")

            # pass word to callback to get possible matches
            matches = self.get_matches(word)

            if matches:
                # autocomplete on the first match
                remainder = matches[0][len(word):]

                # remember the current insertion cursor
                insert = self.index("insert")

                # insert at the insertion cursor the remainder of
                # the matched word, and apply the tag "sel" so that
                # it is selected. Also, add the "autocomplete" text
                # which will make it easier to find later.
                self.insert(insert, remainder, ("sel", "autocomplete"))

                # move the cursor to the end of the autofilled word
                self.mark_set("insert", f"{insert}+{len(remainder)}c")

    def get_matches(self, word):
        # Check if word is in the uvm_classes list
        if word.startswith("uvm_"):
            matches = [x for x in self._uvm_classes if x.startswith(word)]
        else:
            matches = []
        return matches

root = tk.Tk()
root.title('UVMAutocompleter')
root.geometry('600x400')

# List of uvm_classes
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

text = UVMAutocompleter(root, uvm_classes=uvm_classes)
text.pack(fill="both", expand=True)

root.mainloop()
