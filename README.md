# WorkingRepo
Working repo test fork

To create the repo to an individual user's acount:

```
curl -u "your_github_username" -X POST \
  -d '{"name":"WorkingRepo"}' \
  https://api.github.com/repos/Softala-MLOPS/ConfigRepo/forks
```

To create the repo into a specific organisation:

```
curl -u "your_github_username" -X POST \
  -d '{"organization":"organization_name", "name":"WorkingRepo"}' \
  https://api.github.com/repos/Softala-MLOPS/ConfigRepo/forks
```


****
```
