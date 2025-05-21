.PHONY: post-clone

post-clone:
	git remote add kohya-ss https://github.com/kohya-ss/FramePack-LoRAReady.git
	git fetch kohya-ss
	git branch | grep -q "kohya-ss/LoRAReady" || git branch kohya-ss/LoRAReady
	git merge kohya-ss/main kohya-ss/LoRAReady
