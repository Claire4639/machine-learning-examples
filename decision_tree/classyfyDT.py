def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer

    from sklearn import tree
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features_train, labels_train)


    from sklearn.metrics import accuracy_score
    pred = clf.predict(features_test)
    acc = accuracy_score(pred, labels_test)
    print acc
  
    return clf