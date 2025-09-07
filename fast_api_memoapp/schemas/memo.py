from pydantic import BaseModel, Field

class InsertAndUpdateMemoSchema(BaseModel) :
    title : str = Field(...,
                        description='メモのタイトルを入力してください。少なくとも1文字以上必要です。',
                        example = '明日のアジェンダ', min_length = 1)
    description : str = Field(...,
                            description = 'メモの内容についての追加情報',
                            example = '会議で話すトピック:プロジェクトの進行状況')
    
class MemoSchema(BaseModel):
    memo_id :int = Field(...,
                        description='メモを一意に識別するID番号.データベースで自動的に割り当てられます。',
                        example = 123)
    
class ResponseSchema(BaseModel) :
    message :str = Field(...,
                        description = 'APIの操作の結果を説明するメッセージ。',
                        example = 'メモの更新に成功しました')