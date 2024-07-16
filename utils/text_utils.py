import textwrap


def to_markdown(text):
    """Converts text to a Markdown-friendly format with indented bullet points."""
    text = text.replace("•", "*")  # Replace bullet points with Markdown asterisks
    return textwrap.indent(text, "> ", predicate=lambda _: True)
