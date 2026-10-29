## create a new repository on the command line

```bash
echo "# mon_super_flask" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fduranddev/mon_super_flask.git
git push -u origin main
```

## push an existing repository from the command line

```bash
git remote add origin https://github.com/fduranddev/mon_super_flask.git
git branch -M main
git push -u origin main
```