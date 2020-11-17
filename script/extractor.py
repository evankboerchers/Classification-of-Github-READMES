import pandas


def load_section_overview_from_csv(input_filename_csv):
    df = pandas.read_csv(input_filename_csv, header=0, delimiter=',',
                     names=['section_id','file_id','url','heading_markdown','section_code'])
    
    readme_file_generator = lambda x: x.replace('https://github.com/','').replace('/','.') + '.md'
    df['local_readme_file'] = df['url'].apply(readme_file_generator) 
    # df['heading_text'] = df['heading_markdown'].apply(extract_text_in_heading_markdown)
    # In markdown, # = heading level 1, ## = heading level 2, etc.
    df['heading_level'] = df['heading_markdown'].apply(lambda x : len(re.search('^#+', x).group(0)))
    # df['abstracted_heading_markdown'] = df['heading_markdown'].apply(lambda x : abstract_text(x).replace('\n', ' ').strip())
    # df['abstracted_heading_text'] = df['abstracted_heading_markdown'].apply(extract_text_in_heading_markdown)
    # Don't convert to int, as data contains '-' for 'not in any class'
    # df['section_code'] = df['section_code'].apply(lambda x : merge_classes_1_and_2(x))
    
    return df
        