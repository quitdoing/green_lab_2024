from unittest.mock import MagicMock

globals = MagicMock()

sentences = MagicMock()
encoded_input = MagicMock()
torch = MagicMock()
all_embeddings = []
key = MagicMock()
batch_size = 32
self = MagicMock()
self.device = 'cuda'
self.tokenizer = MagicMock()
self.model = MagicMock()

sentences = ["This is sentence {}".format(i) for i in range(100000 * 10)] 

print("Loop is starting...")
for i in range(0, len(sentences), batch_size):
    batch_sentences = sentences[i:i + batch_size]
    
    encoded_input = self.tokenizer(batch_sentences, padding=True,
        truncation=True, return_tensors='pt')
    
    encoded_input = {key: tensor.to(self.device) for key, tensor in
        encoded_input.items()}
    
    with torch.no_grad():
        model_output = self.model(**encoded_input)
    
    embeddings = model_output.last_hidden_state.mean(dim=1)
    
    all_embeddings.append(embeddings)

all_embeddings = torch.cat(all_embeddings).cpu().numpy()

print("Loop has finished.")
