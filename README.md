This repository is used to run Talvos through the Vulkan Conformance
Test Suite (CTS) on a regular basis, via the cloud. The CTS takes too
long to run for all commits and pull requests in the main Talvos
repository, so we run it once per day here instead.

Results for commit dba491f on Thu 13 Dec 2018
-----------------------------------------------
api                 :  11380 /  81012 ->  14.0%
binding_model       :  15795 /  43207 ->  36.6%
clipping            :      3 /    166 ->   1.8%
compute             :     40 /     68 ->  58.8%
device_group        :      0 /     12 ->   0.0%
draw                :     40 /    515 ->   7.8%
dynamic_state       :      0 /     15 ->   0.0%
fragment_operations :      9 /     35 ->  25.7%
geometry            :      0 /    136 ->   0.0%
glsl                :   6072 /  16806 ->  36.1%
image               :   1590 /  11762 ->  13.5%
info                :      4 /      4 -> 100.0%
memory              :   1579 /   2817 ->  56.1%
multiview           :      0 /    324 ->   0.0%
pipeline            :   3142 /  83303 ->   3.8%
protected_memory    :      0 /   4351 ->   0.0%
query_pool          :      0 /    372 ->   0.0%
rasterization       :     40 /    160 ->  25.0%
renderpass          :    604 /  13297 ->   4.5%
renderpass2         :      0 /   8534 ->   0.0%
robustness          :    696 /    762 ->  91.3%
sparse_resources    :      0 /   1636 ->   0.0%
spirv_assembly      :   2014 /  12045 ->  16.7%
ssbo                :   1681 /   1685 ->  99.8%
subgroups           :      0 /   6053 ->   0.0%
synchronization     :    962 /  23409 ->   4.1%
tessellation        :      0 /    432 ->   0.0%
texture             :      0 /   5028 ->   0.0%
ubo                 :   1531 /   2291 ->  66.8%
wsi                 :      0 /    455 ->   0.0%
ycbcr               :      0 /  20923 ->   0.0%
-----------------------------------------------
Total tests passed  :  47182 / 341615 ->  13.8%
-----------------------------------------------
