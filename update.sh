#!/bin/bash
sudo chown -R $USER:$USER .
git stash push
git fetch --all
git reset --hard origin/main
chown -R $USER:$USER .