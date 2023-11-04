def get_entry_number(message_content):
    try:
        convert_to_int = int(message_content[9:])
        return convert_to_int
    except ValueError:
        return 0