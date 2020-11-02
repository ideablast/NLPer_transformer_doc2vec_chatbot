# NLPer_chatbot

epoch : 50

validation set: 0.1

batch_size : 64

lstm_hidden_state_dim : 100


RE_FILTER = re.compile("[\"':;~()]")

 - w2v를 써봤을때의 결과는 매우 실망스러웠음.

### Transformer로 모델 변경 + 그외 잡기술(dropout, layernormalization, Adam with custom learning rate)
 - 20 epoch의 결과 : 나름 일반적인 모델
 - 50 epoch의 결과 : overfitting의 기질이 보임. train data는 잘 맞추지만, 못본 문장은 조금 약한거 같기도?
 
 ### Transformer + Pretrained Embedding model(w2v, 50M, 200D)
  - 50 에폭 결과 기존 Transformer(Okt)와 미미한 
