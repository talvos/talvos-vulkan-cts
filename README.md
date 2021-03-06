This repository is used to run Talvos through the Vulkan Conformance
Test Suite (CTS) on a regular basis, via the cloud. The CTS takes too
long to run for all commits and pull requests in the main Talvos
repository, so we run it once per day here instead.

```
Results for commit f2f134e on Thu 11 Jul 2019
---------------------------------------------------
api                     :  22010 /  87914 ->  25.0%
binding_model           :  16355 /  44782 ->  36.5%
clipping                :      3 /    294 ->   1.0%
compute                 :     43 /     68 ->  63.2%
conditional_rendering   :      0 /    144 ->   0.0%
device_group            :      6 /     12 ->  50.0%
draw                    :     52 /    515 ->  10.1%
dynamic_state           :      0 /     15 ->   0.0%
fragment_operations     :     10 /     35 ->  28.6%
geometry                :      0 /    136 ->   0.0%
glsl                    :   9935 /  17715 ->  56.1%
image                   :   4014 /  20810 ->  19.3%
info                    :      4 /      4 -> 100.0%
memory                  :   1627 /   2828 ->  57.5%
memory_model            :      0 /   5566 ->   0.0%
multiview               :      0 /    324 ->   0.0%
pipeline                :   4246 /  86150 ->   4.9%
protected_memory        :      0 /   4357 ->   0.0%
query_pool              :      0 /    372 ->   0.0%
rasterization           :     41 /    157 ->  26.1%
renderpass              :    622 /  12704 ->   4.9%
renderpass2             :      0 /  13106 ->   0.0%
robustness              :    738 /    762 ->  96.9%
sparse_resources        :      0 /   1636 ->   0.0%
spirv_assembly          :   3350 /  25542 ->  13.1%
ssbo                    :   1930 /   3954 ->  48.8%
subgroups               :      0 /   6053 ->   0.0%
synchronization         :   1691 /  23409 ->   7.2%
tessellation            :      0 /    432 ->   0.0%
texture                 :      0 /   7836 ->   0.0%
ubo                     :   2568 /   8965 ->  28.6%
wsi                     :      0 /    471 ->   0.0%
ycbcr                   :      3 /  20923 ->   0.0%
---------------------------------------------------
Total tests passed      :  69248 / 397991 ->  17.4%
Total tests failed      :   5963 / 397991 ->   1.5%
Total tests crashed     :  92405 / 397991 ->  23.2%
Total tests timedout    :     18 / 397991 ->   0.0%
Total tests warned      :     41 / 397991 ->   0.0%
Total tests unsupported : 230316 / 397991 ->  57.9%
---------------------------------------------------
Supported tests passed  :  69248 / 167675 ->  41.3%
---------------------------------------------------
```
