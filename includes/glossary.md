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
*[one-hot]: Turning each DNA base into a column of four slots with a 1 in the A, C, G, or T slot and zeros elsewhere, so a sequence becomes a 4-by-length matrix a network can read
*[track]: One number per genomic position from one assay in one cell type — the coverage profile a sequence model is trained to reproduce
*[receptive field]: The stretch of input sequence that can actually influence one output position, usually far shorter than the window the model is fed
*[position weight matrix]: A table of per-position base preferences for a binding motif; scanning it along a sequence is the same operation a convolution filter performs
*[PWM]: Position weight matrix: a table of per-position base preferences for a motif, scanned along a sequence exactly as a convolution filter is
*[motif]: The short, recurring sequence pattern a protein such as a transcription factor prefers to bind
*[in silico mutagenesis]: Changing one or more bases in the input and rereading the model's output, to estimate what that mutation does
*[ISM]: In silico mutagenesis: changing bases in the input and rereading the model's output to estimate a mutation's effect
*[eQTL]: A genetic variant statistically associated with the expression level of a gene, measured across a population
*[caQTL]: A genetic variant statistically associated with how open (accessible) a stretch of chromatin is
*[MPRA]: Massively parallel reporter assay — a method that measures the regulatory activity of tens of thousands to millions of designed DNA sequences at once
*[CRISPRi]: CRISPR interference — silencing a specific regulatory element so you can measure, causally, what it controls
*[pseudobulk]: Pooling many single cells of the same type into one aggregate profile, to get a cleaner signal than any single sparse cell gives
*[ATAC-seq]: An assay that reads which stretches of DNA are open and accessible across the genome
*[ChIP-seq]: An assay that reads where a particular protein sits on the genome
*[CAGE]: An assay that reads where transcription starts, by capturing the 5' ends of RNAs
*[coding agent]: A program that runs a language model in a loop with tools, so it can read your files, run commands and edit code instead of only answering questions
*[harness]: The tools, context management and execution environment wrapped around a model to make it an agent; Claude Code is the harness, Claude is the model inside it
*[MCP]: An open standard, now stewarded by the Linux Foundation, that lets any agent connect to outside systems such as databases through one common interface
*[diff]: The exact line-by-line changes between two versions of a file, which is what git shows you and what lets you undo them
*[SSH]: A secure way to log in to another computer over the network and run commands on it, such as a remote server or compute cluster
*[HPC cluster]: A shared high-performance computing system of many networked machines you send heavy jobs to, instead of running them on your laptop
*[login node]: The shared entry-point machine you land on when you connect to a cluster, meant for editing and submitting jobs rather than running heavy computation
