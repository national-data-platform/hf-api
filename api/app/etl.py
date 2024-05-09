from huggingface_hub import list_models,ModelCard

THRESHOLD_DOWNLOADS = 10000

def get_models():
    models = list_models(full=True)

    keys = ['modelId','author','created_at','private',
            'downloads','tags','library_name','text',
            'content']
    model_data = []

    for model in models:
        iModel = dict.fromkeys(keys)
        iModel['modelId'] = model.id
        iModel['author'] = model.author
        iModel['created_at'] = model.created_at
        iModel['downloads'] = model.downloads
        iModel['private'] = model.private
        iModel['tags'] = model.tags
        iModel['library_name'] = model.library_name
        iModel['text'] = ''
        iModel['content'] = ''
        if model.downloads >= THRESHOLD_DOWNLOADS:
            try:
                #For the cases with 404, card not found
                card = ModelCard.load(model.id)
                iModel['text'] = card.text
                iModel['content'] = card.content
            except:
                iModel['text'] = ''
                iModel['content'] = ''
        model_data.append(iModel)
    return model_data