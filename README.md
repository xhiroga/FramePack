# FramePack-Dev

FramePack-Dev is a fork that adds the following features to FramePack and FramePack LoRAReady.

- Standalone execution. Run `uv run demo_gradio.py`
- Add extra model directories. `--extra-model-paths-config`
- Embedding metadata to the generated video.

## Disclaimer

I have no intention of maintaining this repository for a long time.  
I believe that the new features implemented in this repository should be incorporated into the FramePack ecosystem and ComfyUI.  

Developers are free to use the code in this repository.

## How to run

```sh
uv run demo_gradio.py --extra-model-paths-config extra_model_paths.yaml
```

## Original

Thanks to the efforts of lllyasviel, kohya-ss, and many others.

- [FramePack](https://github.com/lllyasviel/FramePack)
- [FramePack LoRAReady](https://github.com/kohya-ss/FramePack-LoRAReady)
