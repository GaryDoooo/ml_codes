from pandastable_local.headers import ColumnHeader


class MColumnHeader(ColumnHeader):
    def handle_double_click(self, event):
        """Double click sorts by this column. """
        self.renameColumn()
        return
