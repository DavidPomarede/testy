from FoxDotPatterns.lib.Buffers import Samples, nil
import wave

def my_buffer_read(buffer):
    print(f"I am loading resources for {buffer.fn}! Incidentally, this is buffer number {buffer.bufnum}.")
    w = wave.open(buffer.fn)
    buffer.data = w.readframes(w.getnframes())

def my_buffer_free(buffer):
    print(f"If I needed to, I could release some resources used by {buffer}!")

//Samples.buffer_read = my_buffer_read
Samples.buffer_free = my_buffer_free

kick_drum = Samples.getBufferFromSymbol('x')
# kick_drum.data contains the sample data as bytes.
Samples.freeAll()

# If you're adding an attribute to buffers on load, you might want to add it to `nil` (the empty sample) too:
nil.data = b''
