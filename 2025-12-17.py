def parse_blockquote(markdown: str):
    cleanup = markdown.lstrip()
    if cleanup.startswith("> "):
        headblock = "<blockquote>" + cleanup.replace(">","").lstrip()
        htmlblock = headblock + "</blockquote>"
        print(htmlblock)
        return htmlblock
    else:
        return markdown
    

assert parse_blockquote("> This is a quote") == "<blockquote>This is a quote</blockquote>"
assert parse_blockquote(" > This is also a quote") == "<blockquote>This is also a quote</blockquote>"
assert parse_blockquote("  >    So  Is  This") == "<blockquote>So  Is  This</blockquote>"