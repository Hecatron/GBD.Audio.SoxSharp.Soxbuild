@echo off

echo Restoring any NuGet Packages
binfiles\NuGet.exe restore scripts\packages.config
