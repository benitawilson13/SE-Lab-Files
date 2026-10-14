import io
import math
import struct
import wave
import pygame


def create_tone(frequency, duration, volume=0.4):
    """
    Create a simple beep sound in memory.
    """
    sample_rate = 44100
    number_of_samples = int(sample_rate * duration)

    audio_data = bytearray()

    for i in range(number_of_samples):
        time = i / sample_rate

        # Create a sine wave
        sample = math.sin(2 * math.pi * frequency * time)

        # Fade out near the end to avoid clicking
        fade = 1.0
        fade_samples = int(sample_rate * 0.02)

        if i > number_of_samples - fade_samples:
            fade = (number_of_samples - i) / fade_samples

        value = int(
            sample * volume * fade * 32767
        )

        audio_data.extend(
            struct.pack("<h", value)
        )

    # Put the audio data into a WAV file in memory
    wav_buffer = io.BytesIO()

    with wave.open(wav_buffer, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_data)

    wav_buffer.seek(0)

    return pygame.mixer.Sound(file=wav_buffer)


def create_eat_sound():
    return create_tone(
        frequency=800,
        duration=0.12,
        volume=0.35
    )


def create_game_over_sound():
    return create_tone(
        frequency=200,
        duration=0.5,
        volume=0.45
    )