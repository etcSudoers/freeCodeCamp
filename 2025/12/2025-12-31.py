"""

Markdown Italic Parser

Given a string that may include some italic text in Markdown, return the equivalent HTML string.

    Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
    There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
    Convert all italic occurrences to HTML i tags and return the string.

For example, given "*This is italic*", return "<i>This is italic</i>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

"""
import markdown 

def parse_italics(markdowntext):
    html = markdown.markdown(markdowntext)
    html = html.replace("<em>", "<i>").replace("</em>", "</i>")
    html = html.replace("<p>", "").replace("</p>", "")



    return html




parse_italics("*This is italic*") == "<i>This is italic</i>"
parse_italics("_This is also italic_") == "<i>This is also italic</i>"
parse_italics("*This is not italic *") == "*This is not italic *"
parse_italics("_ This is also not italic_") == "_ This is also not italic_"
parse_italics("The *quick* brown fox _jumps_ over the *lazy* dog.") == "The <i>quick</i> brown fox <i>jumps</i> over the <i>lazy</i> dog."