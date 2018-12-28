This repository is used to run Talvos through the Vulkan Conformance
Test Suite (CTS) on a regular basis, via the cloud. The CTS takes too
long to run for all commits and pull requests in the main Talvos
repository, so we run it once per day here instead.

```
Results for commit bf1c357 on Fri 28 Dec 2018
---------------------------------------------------
api                     :  15294 /  81011 ->  18.9%
binding_model           :  15795 /  44782 ->  35.3%
clipping                :      3 /    166 ->   1.8%
compute                 :     43 /     68 ->  63.2%
device_group            :      6 /     12 ->  50.0%
draw                    :     52 /    395 ->  13.2%
dynamic_state           :      0 /     15 ->   0.0%
fragment_operations     :     10 /     35 ->  28.6%
geometry                :      0 /    136 ->   0.0%
glsl                    :   9791 /  17427 ->  56.2%
image                   :   3152 /  15770 ->  20.0%
info                    :      4 /      4 -> 100.0%
memory                  :   1585 /   2817 ->  56.3%
memory_model            :      0 /   5566 ->   0.0%
multiview               :      0 /    324 ->   0.0%
pipeline                :   3427 /  83287 ->   4.1%
protected_memory        :      0 /   4351 ->   0.0%
query_pool              :      0 /    372 ->   0.0%
rasterization           :     41 /    160 ->  25.6%
renderpass              :    610 /  13297 ->   4.6%
renderpass2             :      0 /   8534 ->   0.0%
robustness              :    696 /    762 ->  91.3%
sparse_resources        :      0 /   1636 ->   0.0%
spirv_assembly          :   2777 /  23983 ->  11.6%
ssbo                    :   1930 /   3948 ->  48.9%
subgroups               :      0 /   6053 ->   0.0%
synchronization         :   1339 /  23409 ->   5.7%
tessellation            :      0 /    428 ->   0.0%
texture                 :      0 /   4996 ->   0.0%
ubo                     :   2567 /   8965 ->  28.6%
wsi                     :      0 /    455 ->   0.0%
ycbcr                   :      0 /  20923 ->   0.0%
---------------------------------------------------
Total tests passed      :  59122 / 374087 ->  15.8%
Total tests failed      :   5360 / 374087 ->   1.4%
Total tests crashed     :  93867 / 374087 ->  25.1%
Total tests timedout    :     15 / 374087 ->   0.0%
Total tests warned      :     41 / 374087 ->   0.0%
Total tests unsupported : 215682 / 374087 ->  57.7%
---------------------------------------------------
Supported tests passed  :  59122 / 158405 ->  37.3%
---------------------------------------------------
```
