import sys

sys.path.append("..")
from pycorrector.macbert.macbert_corrector import MacBertCorrector

import spacy

nlp = spacy.load("zh_core_web_sm")

def split_sentences(text):
    """将大段中文文本分割为句子列表"""
    # 预处理文本，移除换行符和制表符
    text = text.replace('\n', '').replace('\t', '')
    doc = nlp(text)
    # 获取句子并删除每个句子中的空格和双引号
    return [sent.text.strip().replace(' ', '').replace('“', '').replace('”', '').lower() for sent in doc.sents]
 
long_text = """你找到你最喜欢的工作，我也很高心
"""
sentences = split_sentences(long_text)


if __name__ == '__main__':
    error_sentences = sentences

    m = MacBertCorrector("shibing624/macbert4csc-base-chinese")
    for i, sent in enumerate(sentences):
        print(f"{i+1}. {sent}")
    
    print("\n开始纠错:")
    for line in sentences:
        try:
            # 确保输入不为空
            if not line.strip():
                continue
            # 进行纠错
            correct_sent, err = m.macbert_correct(line)
            if err!= []:
                # 打印结果
                print('-----------------------------------------********************------------------------')
                print("原文: {}".format(line))
                print("纠正: {}".format(correct_sent))
                print("错误: {}".format(err))
        except Exception as e:
            print(f"处理句子时出错: {line}")
            print(f"错误信息: {e}")
