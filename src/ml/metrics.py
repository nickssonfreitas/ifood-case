import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

def precision_at_k(y_true, y_score, k=100):
    """
    Calcula Precision@K
    """
    top_k_idx = np.argsort(y_score)[::-1][:k]
    y_pred_topk = np.zeros_like(y_true)
    y_pred_topk[top_k_idx] = 1
    return round(precision_score(y_true, y_pred_topk, zero_division=0), 4)

def recall_at_k(y_true, y_score, k=100):
    """
    Calcula Recall@K
    """
    top_k_idx = np.argsort(y_score)[::-1][:k]
    y_pred_topk = np.zeros_like(y_true)
    y_pred_topk[top_k_idx] = 1
    return round(recall_score(y_true, y_pred_topk, zero_division=0), 4)

def f1_at_k(y_true, y_score, k=100):
    """
    Calcula F1-Score@K
    """
    top_k_idx = np.argsort(y_score)[::-1][:k]
    y_pred_topk = np.zeros_like(y_true)
    y_pred_topk[top_k_idx] = 1
    return round(f1_score(y_true, y_pred_topk, zero_division=0), 4)
