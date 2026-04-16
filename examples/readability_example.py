from blogger_toolkit.content.readability import calculate_readability

text = open("examples/sample_blog_post.txt", encoding="utf-8").read()
print(calculate_readability(text))
