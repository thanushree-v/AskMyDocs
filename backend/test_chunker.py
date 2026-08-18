from app.rag.chunker import chunk_text

sample_text = """
Operating systems manage computer hardware and software resources.
They provide services for computer programs.
Processes are programs in execution.

Deadlock is a situation where a group of processes are permanently blocked.
Each process is waiting for a resource held by another process.
There are four necessary conditions for deadlock.
"""

chunks = chunk_text(sample_text)

print("Number of chunks:",len(chunks))

for i,chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)