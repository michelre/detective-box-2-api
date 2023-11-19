prod:
	rsync -av -e ssh --exclude='.git' --exclude='venv' --exclude='.github' * root@164.92.202.230:/data/detectivebox/api/
