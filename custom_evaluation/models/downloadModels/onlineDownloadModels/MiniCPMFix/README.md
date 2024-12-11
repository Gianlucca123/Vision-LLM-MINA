https://huggingface.co/openbmb/MiniCPM-V-2/discussions/23

# Replacing `modeling_minicpm.py` in the `.cache` Directory

## Overview
This guide explains how to replace the `modeling_minicpm.py` file in the `.cache` directory with the provided version to fix an issue related to the generation code in the MiniCPM-V-2 model.

## Problem Description
The issue arises in the `prepare_inputs_for_generation` function at line 1489 of the `modeling_minicpm.py` file located in the `.cache` directory. Specifically, the problem occurs when `inputs_embeds` is not `None` and `past_key_values` is empty but not `None`. This leads to an `IndexError` when calculating the rotary embedding.

### Fix 1
Replace `modeling_minicpm.py` located in : **.cache/huggingface/modules/transformers_modules/openbmb/MiniCPM-V-2/.../modeling_minicpm.py**
With the attached `modeling_minicpm.py` file.

### Fix 2
Replace line 1489, in `modeling_minicpm.py`, `prepare_inputs_for_generation` from :
`if inputs_embeds is not None and past_key_values is None:` to `if inputs_embeds is not None and past_length==0:`