# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from typing import Optional
import sys
import fire

from llama import Llama
import json

def main(
    ckpt_dir: str,
    tokenizer_path: str,
    dialog:str, 
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 4,
    max_gen_len: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    print(dialog, type(dialog))
    dialog = [dialog] 
    results = generator.chat_completion(
        dialog,  # type: ignore
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    output = {}
    output['role'] = results[0]['generation']['role']
    output['content'] = results[0]['generation']['content']
    sys.stdout.write(json.dumps(output))

if __name__ == "__main__":
    fire.Fire(main)
