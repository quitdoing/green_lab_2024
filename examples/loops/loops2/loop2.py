from unittest.mock import MagicMock, AsyncMock
import asyncio
for i in range(5000):
    time = MagicMock()
    time.time.return_value = 1234567890.0

    text_data = MagicMock()
    audio_data = MagicMock()
    q_done = False
    ev = MagicMock()
    self = MagicMock()

    self._text_q_changed = asyncio.Event()
    self._audio_q_changed = asyncio.Event()

    self._text_q = [text_data, None]
    self._audio_q = [audio_data, None]
    self._closed = False
    self._playing_seg_index = 0

    self._sync_sentence_co = AsyncMock()

    async def run_loop():
        global q_done
        seg_index = 0
        #print("Loop is starting...")

        while not q_done:  
            await self._text_q_changed.wait() 
            await self._audio_q_changed.wait() 

            while self._text_q and self._audio_q:
                text_data = self._text_q.pop(0)
                audio_data = self._audio_q.pop(0)

                if text_data is None or audio_data is None:
                    q_done = True
                    continue

                while not self._closed:
                    if self._playing_seg_index >= seg_index:
                        break
                    await asyncio.sleep(0.125)

                sentence_stream = text_data.sentence_stream
                forward_start_time = time.time()

                async for ev in sentence_stream:
                    await self._sync_sentence_co(
                        seg_index, forward_start_time, text_data, audio_data, ev.token, MagicMock()
                    )

                seg_index += 1

            self._text_q_changed.clear()
            self._audio_q_changed.clear()

        #print("Loop has finished.")

    text_data.sentence_stream = AsyncMock()
    text_data.sentence_stream.__aiter__.return_value = [ev]

    self._text_q_changed.set()
    self._audio_q_changed.set()

    asyncio.run(run_loop())
