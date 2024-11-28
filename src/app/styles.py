def apply_styles(root):
    root.config(bg="#f0f0f0")
    root.option_add("*Font", "Helvetica 12")
    root.option_add("*Button.bg", "#4CAF50")
    root.option_add("*Button.fg", "white")
    root.option_add("*Button.activeBackground", "#45a049")
    root.option_add("*Button.activeForeground", "white")
    root.option_add("*Button.borderWidth", 2)
    root.option_add("*Button.padding", [10, 5])

    # Apply styles to entry widget
    root.option_add("*Entry.bg", "#ffffff")
    root.option_add("*Entry.fg", "#000000")
    root.option_add("*Entry.borderWidth", 1)

    # Apply styles to labels
    root.option_add("*Label.bg", "#f0f0f0")
    root.option_add("*Label.fg", "#333333")
