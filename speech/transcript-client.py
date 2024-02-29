from whisper_live.client import TranscriptionClient

client = TranscriptionClient(
    "localhost",
    9090,
    lang="en",
    translate=True,
    model="small",
    use_vad=False,
)

client()