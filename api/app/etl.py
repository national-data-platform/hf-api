from huggingface_hub import list_models

def get_models():
    models = list_models()

    keys = ['modelId','created_at','private','downloads','tags','library_name']
    model_data = []

    for model in models:
        iModel = dict.fromkeys(keys)
        iModel['modelId'] = model.id
        # iModel['author'] = model.author
        iModel['created_at'] = model.created_at
        iModel['downloads'] = model.downloads
        iModel['private'] = model.private
        iModel['tags'] = model.tags
        iModel['library_name'] = model.library_name
        model_data.append(iModel)
    return model_data