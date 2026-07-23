# Glossary (English)

Definitions used for hover tooltips across the site — see `hooks/glossary.py`.
The Chinese counterpart is `glossary.zh.md`; keep the two in sync.

Two rules:

- One line per term, `*[term]: definition`. Keep the definition to a single
  sentence — it has to fit in a tooltip.
- A concept that has (or will have) its own page gets an **internal link** in
  the prose instead of an entry here. No entries for AlphaFold, AlphaGenome, and
  the like.

*[neural network]: A stack of simple numeric transformations whose parameters are learned from data rather than written by hand
*[deep learning]: Machine learning with neural networks many layers deep, where the useful features are learned instead of hand-designed
*[tensor]: The n-dimensional array that holds all data and parameters in a neural network — a matrix with any number of axes
*[gradient descent]: The training loop itself: nudge every parameter a little in the direction that reduces the error, over and over
*[backpropagation]: The chain rule applied backwards through a network to work out how much each parameter contributed to the error
*[automatic differentiation]: The framework feature that computes those derivatives for you, so you only ever write the forward computation
*[overfitting]: When a model memorises its training data and gets worse on anything it has not seen
*[multilayer perceptron]: The plainest neural network — a few fully connected layers stacked with a nonlinearity between them
*[MLP]: Multilayer perceptron: the plainest neural network, a few fully connected layers with a nonlinearity between them
*[convolutional neural network]: A network that slides a small filter across its input, so it can spot the same local pattern anywhere it occurs
*[CNN]: Convolutional neural network: slides a small filter across the input, so it spots the same local pattern wherever it occurs
*[recurrent neural network]: A network that walks along a sequence one step at a time, carrying a running summary of everything it has read
*[RNN]: Recurrent neural network: walks along a sequence one step at a time, carrying a running summary of what it has read
*[attention]: A mechanism that lets a model decide, for each position, which other positions are worth looking at instead of treating them equally
*[Transformer]: The attention-based architecture introduced in 2017 that is now the backbone of large language models and most biological sequence models
*[embedding]: A learned list of numbers standing in for something discrete — a word, a gene, a cell — placed so that similar things sit close together
*[pre-training]: Training a large model once on a huge generic dataset, producing a starting point that many downstream tasks can reuse
*[pre-trained]: Already trained once on a huge generic dataset, so it can serve as a starting point for many downstream tasks
*[fine-tuning]: Taking a pre-trained model and training it a little further on your own smaller dataset
*[fine-tuned]: Taken as a pre-trained model and trained a little further on a smaller, task-specific dataset
*[large language model]: A very large Transformer pre-trained on text, which is why it can be prompted to do tasks it was never explicitly trained on
*[LLM]: Large language model: a very large Transformer pre-trained on text, promptable for tasks it was never explicitly trained on
