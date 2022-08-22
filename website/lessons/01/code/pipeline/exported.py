def tags_len(tags):
    return len(tags)

def parse_tags(tags):
    if not tags:
        return {}
    
    # we'll only process the first three     
    to_process = tags[:3]
    
    # convert: [[key0, value0], [key1, value1], ...]
    # into: [key0, key1, ...], [value0, value1, ...], 
    keys, values = zip(*to_process[:3])
    
    # convert to: column_name: key
    keys_mapping = {f'tag_{i}': k for i, k in enumerate(keys)}
    # convert to: column_name: value
    values_mapping = {f'value_{i}': k for i, k in enumerate(values)}
    
    return {**keys_mapping, **values_mapping}