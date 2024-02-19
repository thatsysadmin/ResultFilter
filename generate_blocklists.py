import os

# Get filter templates
filter_template_list = []
filter_templates = os.listdir("./filter_templates")
for filter_template_filename in filter_templates:
    print("Processing filter templates in " + filter_template_filename)
    filter_template_file = open("./filter_templates/" + filter_template_filename)
    while True:
        template = filter_template_file.readline()
        if template == "":
            break
        else:
            filter_template_list.append(template)

# Build filter lists
filter_list = []
domain_lists = os.listdir("./domain_lists")
for domain_list_filename in domain_lists:
    print("Processing list " + domain_list_filename)
    domain_list_file = open("./domain_lists/" + domain_list_filename)
    while True:
        domain = domain_list_file.readline()
        if domain == "":
            break
        for template in filter_template_list:
            cache = template.replace("$SITENAME", domain)
            filter_list.append(cache)

result_file = open("result.txt", "w")
result_file.writelines(filter_list)
print("Done.")