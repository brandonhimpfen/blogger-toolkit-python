from blogger_toolkit.seo.keyword_density import calculate_keyword_density

text = open("examples/sample_blog_post.txt", encoding="utf-8").read()
keywords = ["blogging", "workflow", "metadata"]

print(calculate_keyword_density(text, keywords))
