# easy-anki

根据 *Forgetting curve* 对 database 中的 materials 进行测试和评分, 从而巩固你的 memory.

目前仅考虑从 Japanese 学习的 angle 进行简单的 functionaly design.

首先, 以 Japanese 中的 words, phrases 或 sentences 为单位, 将其 store 在 databases 中, 比如 sqlite. 字段可能 involes:

1. `id`: 该记录的 identifier
2. `type`: 表明该 record 是 word, phrase 还是 sentence
3. `original_content`: 对应 word, phrase 或 sentence 的原生 content
4. `romaji_content`: 对应 word, phrase 或 sentence 的罗马字 content
5. `translated_content`: 对应 word, phrase 或 sentence 翻译为 Chinese 的 content
6. `explanation`: 关于该 record 的 explanation
7. `inserted_date`: 该条 record 被 inserted 时的 date
8. `test_times`: 该条 record 被 test 的次数
9. `success_times`: 该条 record 测试成功的次数
10. `last_review_date`: 该条 record 最后一次被 test 的 date
11. `memory_strength`: 该条 record 的记忆强度
12. `ease_factor`: 该条 record 的难度系数
13. `next_review_date`: 下次 review 的 date


随后, application 会从 database 中获取 `translated_content` 与 `explanation` 并将其展示给 user 作为 question. 此时用户需要输入 content 作为 answer, 如果:

- 用户的 answer 与 `original_content` 的 content 一致, 那么 `test_times` 与 `success_times` 均增加 1. 
- 用户的 answer 与 `original_content` 的 content 不一致, 那么 `test_times` 增加 1. 
- 用户没有 input 任何 content, 直接 enter 表示跳过, 那么 `test_times` 增加 1.(视为 failure)

同时更新 `last_review_date` 的 date.

接着, application 会展示 `original_content` 和 `romaji_content` 以供参考, 并同时要求用户对本次 review 进行评价, 随后进入下一轮 review.