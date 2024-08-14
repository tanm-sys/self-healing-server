import numpy as np
import structlog
from sklearn.ensemble import IsolationForest

logger = structlog.get_logger()

def detect_anomalies(data):
    try:
        clf = IsolationForest(contamination=0.1)
        preds = clf.fit_predict(data)
        anomalies = np.where(preds == -1)[0]
        return anomalies
    except Exception as e:
        logger.error("Failed to detect anomalies", error=str(e))
        return []
