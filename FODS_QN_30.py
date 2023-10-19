import matplotlib.pyplot as plt
import numpy as np

study_time = np.array([2, 3, 5, 1, 4, 6, 7, 8, 9, 10])
exam_scores = np.array([65, 75, 70, 58, 80, 85, 88, 92, 94, 98])

correlation_coefficient = np.corrcoef(study_time, exam_scores)[0, 1]

plt.figure(figsize=(8, 6))
plt.scatter(study_time, exam_scores, color='b', label=f'Correlation: {correlation_coefficient:.2f}')
plt.title('Study Time vs. Exam Scores')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Scores')
plt.legend()
plt.show()
