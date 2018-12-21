This repository is used to run Talvos through the Vulkan Conformance
Test Suite (CTS) on a regular basis, via the cloud. The CTS takes too
long to run for all commits and pull requests in the main Talvos
repository, so we run it once per day here instead.

```
Results for commit 00e4472 on Fri 21 Dec 2018
-----------------------------------------------
api                 :  14574 /  81012 ->  18.0%
binding_model       :  15795 /  43207 ->  36.6%
clipping            :      3 /    166 ->   1.8%
compute             :     43 /     68 ->  63.2%
device_group        :      0 /     12 ->   0.0%
draw                :     52 /    515 ->  10.1%
dynamic_state       :      0 /     15 ->   0.0%
fragment_operations :     10 /     35 ->  28.6%
geometry            :      0 /    136 ->   0.0%
glsl                :   9645 /  16806 ->  57.4%
image               :   2520 /  11762 ->  21.4%
info                :      4 /      4 -> 100.0%
memory              :   1589 /   2817 ->  56.4%
multiview           :      0 /    324 ->   0.0%
pipeline            :   3427 /  83303 ->   4.1%
protected_memory    :      0 /   4351 ->   0.0%
query_pool          :      0 /    372 ->   0.0%
rasterization       :     41 /    160 ->  25.6%
renderpass          :    604 /  13297 ->   4.5%
renderpass2         :      0 /   8534 ->   0.0%
robustness          :    696 /    762 ->  91.3%
sparse_resources    :      0 /   1636 ->   0.0%
spirv_assembly      :   2250 /  12045 ->  18.7%
ssbo                :   1681 /   1685 ->  99.8%
subgroups           :      0 /   6053 ->   0.0%
synchronization     :   1339 /  23409 ->   5.7%
tessellation        :      0 /    432 ->   0.0%
texture             :      0 /   5028 ->   0.0%
ubo                 :   2290 /   2291 -> 100.0%
wsi                 :      0 /    455 ->   0.0%
ycbcr               :      0 /  20923 ->   0.0%
-----------------------------------------------
Total tests passed  :  56563 / 341615 ->  16.6%
-----------------------------------------------
```
