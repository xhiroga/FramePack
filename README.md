# FramePack-Dev

FramePack-Dev is a fork that adds the following features to FramePack and FramePack LoRAReady.

- Standalone execution. Run `uv run demo_gradio.py`
- Add extra LoRA directories. `--extra-lora-dirs`
- Embedding metadata to the generated video.
- No Windows support. Use WSL2.

## Disclaimer

I have no intention of maintaining this repository for a long time.  
I believe that the new features implemented in this repository should be incorporated into the FramePack ecosystem and ComfyUI.  

Developers are free to use the code in this repository.

## How to run

```console
$ uv run demo_gradio.py --hf-home ~/.cache/huggingface --extra-lora-dirs ~/my_lora_dir
```

## How to see metadata

```console
% ffprobe -v quiet -print_format json -show_format './outputs/250522_sample.mp4'
{
    "format": {
        "filename": "./outputs/250522_sample.mp4",
        "nb_streams": 1,
        "nb_programs": 0,
        "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
        "format_long_name": "QuickTime / MOV",
        "start_time": "0.000000",
        "duration": "2.434000",
        "size": "375246",
        "bit_rate": "1233347",
        "probe_score": 100,
        "tags": {
            "major_brand": "isom",
            "minor_version": "512",
            "compatible_brands": "isomiso2avc1mp41",
            "encoder": "Lavf61.1.100",
            "comment": "{\"prompt\": \"A girl rotates 360 degrees.\", \"n_prompt\": \"\", \"seed\": 31337, \"total_second_length\": 3, \"latent_window_size\": 9, \"steps\": 25, \"cfg\": 1, \"gs\": 10, \"rs\": 0, \"gpu_memory_preservation\": 6, \"use_teacache\": true, \"mp4_crf\": 16, \"lora_file\": \"my_lora.safetensors\", \"lora_multiplier\": 1.5, \"fp8_optimization\": false}"
        }
    }
}
```

## Original

Thanks to the efforts of [@lllyasviel](https://github.com/lllyasviel), [@kohya-ss](https://github.com/kohya-ss), and many others.

- [FramePack](https://github.com/lllyasviel/FramePack)
- [FramePack LoRAReady](https://github.com/kohya-ss/FramePack-LoRAReady)
