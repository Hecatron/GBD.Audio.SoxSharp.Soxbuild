#!/bin/bash

echo Restoring any NuGet Packages
mono binfiles\NuGet.exe restore scripts\packages.config
