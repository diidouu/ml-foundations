#!/bin/bash

for dir in */; do
  # Ignore hidden folders
  [[ "$dir" == .* ]] && continue

  # Remove trailing slash
  folder="${dir%/}"

  # Create README.md if not exists
  if [ ! -f "$folder/README.md" ]; then
    cat << EOF > "$folder/README.md"
# ${folder//_/ }

EOF
  fi

  # Create notes.md if not exists
  if [ ! -f "$folder/notes.md" ]; then
    cat << EOF > "$folder/notes.md"
## Objective

## Problem formulation

## Model / Hypothesis

## Cost function

## Optimization

## Mathematical derivations

## Observations
EOF
  fi
done

echo "README.md and notes.md created in each folder."
