from typing import Dict

from src.python.review.inspectors.issue import IssueType

DETECT_CLASS_NAME_TO_ISSUE_TYPE: Dict[str, IssueType] = {
    # comments
    'CommentOverPrivateFunction': IssueType.BEST_PRACTICES,
    'CommentOverPrivateProperty': IssueType.BEST_PRACTICES,
    'CommentSpacing': IssueType.CODE_STYLE,
    'EndOfSentenceFormat': IssueType.CODE_STYLE,
    'UndocumentedPublicClass': IssueType.BEST_PRACTICES,
    'UndocumentedPublicFunction': IssueType.BEST_PRACTICES,
    'UndocumentedPublicProperty': IssueType.BEST_PRACTICES,

    # complexity:
    'ComplexCondition': IssueType.BOOL_EXPR_LEN,
    'ComplexInterface': IssueType.COMPLEXITY,
    'ComplexMethod': IssueType.COMPLEXITY,
    'LabeledExpression': IssueType.COMPLEXITY,
    'LargeClass': IssueType.COMPLEXITY,
    'LongMethod': IssueType.FUNC_LEN,
    'LongParameterList': IssueType.COMPLEXITY,
    'MethodOverloading': IssueType.COMPLEXITY,
    'NestedBlockDepth': IssueType.COMPLEXITY,
    'StringLiteralDuplication': IssueType.COMPLEXITY,
    'TooManyFunctions': IssueType.COMPLEXITY,

    # coroutines:
    'GlobalCoroutineUsage': IssueType.BEST_PRACTICES,
    'RedundantSuspendModifier': IssueType.BEST_PRACTICES,

    # empty-blocks:
    'EmptyCatchBlock': IssueType.BEST_PRACTICES,
    'EmptyClassBlock': IssueType.CODE_STYLE,
    'EmptyDefaultConstructor': IssueType.BEST_PRACTICES,
    'EmptyDoWhileBlock': IssueType.BEST_PRACTICES,
    'EmptyElseBlock': IssueType.BEST_PRACTICES,
    'EmptyFinallyBlock': IssueType.BEST_PRACTICES,
    'EmptyForBlock': IssueType.BEST_PRACTICES,
    'EmptyFunctionBlock': IssueType.BEST_PRACTICES,
    'EmptyIfBlock': IssueType.BEST_PRACTICES,
    'EmptyInitBlock': IssueType.BEST_PRACTICES,
    'EmptyKtFile': IssueType.BEST_PRACTICES,
    'EmptySecondaryConstructor': IssueType.BEST_PRACTICES,
    'EmptyWhenBlock': IssueType.BEST_PRACTICES,
    'EmptyWhileBlock': IssueType.BEST_PRACTICES,

    # exceptions:
    'ExceptionRaisedInUnexpectedLocation': IssueType.BEST_PRACTICES,
    'InstanceOfCheckForException': IssueType.BEST_PRACTICES,
    'NotImplementedDeclaration': IssueType.BEST_PRACTICES,
    'PrintStackTrace': IssueType.BEST_PRACTICES,
    'RethrowCaughtException': IssueType.BEST_PRACTICES,
    'ReturnFromFinally': IssueType.BEST_PRACTICES,
    'SwallowedException': IssueType.BEST_PRACTICES,
    'ThrowingExceptionFromFinally': IssueType.BEST_PRACTICES,
    'ThrowingExceptionInMain': IssueType.BEST_PRACTICES,
    'ThrowingExceptionsWithoutMessageOrCause': IssueType.BEST_PRACTICES,
    'ThrowingNewInstanceOfSameException': IssueType.BEST_PRACTICES,
    'TooGenericExceptionCaught': IssueType.BEST_PRACTICES,
    'TooGenericExceptionThrown': IssueType.BEST_PRACTICES,

    # naming:
    'ClassNaming': IssueType.CODE_STYLE,
    'ConstructorParameterNaming': IssueType.CODE_STYLE,
    'EnumNaming': IssueType.CODE_STYLE,
    'ForbiddenClassName': IssueType.CODE_STYLE,
    'FunctionMaxLength': IssueType.CODE_STYLE,
    'FunctionMinLength': IssueType.CODE_STYLE,
    'FunctionNaming': IssueType.CODE_STYLE,
    'FunctionParameterNaming': IssueType.CODE_STYLE,
    'InvalidPackageDeclaration': IssueType.ERROR_PRONE,
    'MatchingDeclarationName': IssueType.CODE_STYLE,
    'MemberNameEqualsClassName': IssueType.BEST_PRACTICES,
    'ObjectPropertyNaming': IssueType.CODE_STYLE,
    'PackageNaming': IssueType.CODE_STYLE,
    'TopLevelPropertyNaming': IssueType.CODE_STYLE,
    'VariableMaxLength': IssueType.CODE_STYLE,
    'VariableMinLength': IssueType.CODE_STYLE,
    'VariableNaming': IssueType.CODE_STYLE,

    # performance:
    'ArrayPrimitive': IssueType.BEST_PRACTICES,
    'ForEachOnRange': IssueType.BEST_PRACTICES,
    'SpreadOperator': IssueType.BEST_PRACTICES,
    'UnnecessaryTemporaryInstantiation': IssueType.BEST_PRACTICES,

    # potential-bugs:
    'Deprecation': IssueType.ERROR_PRONE,
    'DuplicateCaseInWhenExpression': IssueType.ERROR_PRONE,
    'EqualsAlwaysReturnsTrueOrFalse': IssueType.ERROR_PRONE,
    'EqualsWithHashCodeExist': IssueType.ERROR_PRONE,
    'ExplicitGarbageCollectionCall': IssueType.ERROR_PRONE,
    'HasPlatformType': IssueType.ERROR_PRONE,
    'ImplicitDefaultLocale': IssueType.ERROR_PRONE,
    'InvalidRange': IssueType.ERROR_PRONE,
    'IteratorHasNextCallsNextMethod': IssueType.ERROR_PRONE,
    'IteratorNotThrowingNoSuchElementException': IssueType.ERROR_PRONE,
    'LateinitUsage': IssueType.ERROR_PRONE,
    'MapGetWithNotNullAssertionOperator': IssueType.ERROR_PRONE,
    'MissingWhenCase': IssueType.ERROR_PRONE,
    'RedundantElseInWhen': IssueType.ERROR_PRONE,
    'UnconditionalJumpStatementInLoop': IssueType.ERROR_PRONE,
    'UnreachableCode': IssueType.ERROR_PRONE,
    'UnsafeCallOnNullableType': IssueType.ERROR_PRONE,
    'UnsafeCast': IssueType.ERROR_PRONE,
    'UselessPostfixExpression': IssueType.ERROR_PRONE,
    'WrongEqualsTypeParameter': IssueType.ERROR_PRONE,

    # style:
    'AnnotationOnSeparateLine': IssueType.CODE_STYLE,
    'ChainWrapping': IssueType.CODE_STYLE,
    'EnumEntryNameCase': IssueType.CODE_STYLE,
    'Filename': IssueType.CODE_STYLE,
    'FinalNewline': IssueType.CODE_STYLE,
    'ImportOrdering': IssueType.CODE_STYLE,
    'Indentation': IssueType.CODE_STYLE,
    'MaximumLineLength': IssueType.CODE_STYLE,
    'ModifierOrdering': IssueType.CODE_STYLE,
    'MultiLineIfElse': IssueType.CODE_STYLE,
    'NoBlankLineBeforeRbrace': IssueType.CODE_STYLE,
    'NoConsecutiveBlankLines': IssueType.CODE_STYLE,
    'NoEmptyClassBody': IssueType.CODE_STYLE,
    'NoEmptyFirstLineInMethodBlock': IssueType.CODE_STYLE,
    'NoLineBreakAfterElse': IssueType.CODE_STYLE,
    'NoLineBreakBeforeAssignment': IssueType.CODE_STYLE,
    'NoMultipleSpaces': IssueType.CODE_STYLE,
    'NoSemicolons': IssueType.CODE_STYLE,
    'NoTrailingSpaces': IssueType.CODE_STYLE,
    'NoUnitReturn': IssueType.CODE_STYLE,
    'NoUnusedImports': IssueType.CODE_STYLE,
    'NoWildcardImports': IssueType.CODE_STYLE,
    'PackageName': IssueType.CODE_STYLE,
    'ParameterListWrapping': IssueType.CODE_STYLE,
    'SpacingAroundColon': IssueType.CODE_STYLE,
    'SpacingAroundComma': IssueType.CODE_STYLE,
    'SpacingAroundCurly': IssueType.CODE_STYLE,
    'SpacingAroundDot': IssueType.CODE_STYLE,
    'SpacingAroundKeyword': IssueType.CODE_STYLE,
    'SpacingAroundOperators': IssueType.CODE_STYLE,
    'SpacingAroundParens': IssueType.CODE_STYLE,
    'SpacingAroundRangeOperator': IssueType.CODE_STYLE,
    'StringTemplate': IssueType.CODE_STYLE,

    # best practices:
    'CollapsibleIfStatements': IssueType.BEST_PRACTICES,
    'DataClassContainsFunctions': IssueType.BEST_PRACTICES,
    'DataClassShouldBeImmutable': IssueType.BEST_PRACTICES,
    'EqualsNullCall': IssueType.BEST_PRACTICES,
    'EqualsOnSignatureLine': IssueType.CODE_STYLE,
    'ExplicitCollectionElementAccessMethod': IssueType.BEST_PRACTICES,
    'ExplicitItLambdaParameter': IssueType.BEST_PRACTICES,
    'ExpressionBodySyntax': IssueType.BEST_PRACTICES,
    'ForbiddenComment': IssueType.BEST_PRACTICES,
    'ForbiddenImport': IssueType.BEST_PRACTICES,
    'ForbiddenMethodCall': IssueType.BEST_PRACTICES,
    'ForbiddenPublicDataClass': IssueType.BEST_PRACTICES,
    'ForbiddenVoid': IssueType.BEST_PRACTICES,
    'FunctionOnlyReturningConstant': IssueType.BEST_PRACTICES,
    'LibraryCodeMustSpecifyReturnType': IssueType.BEST_PRACTICES,
    'LoopWithTooManyJumpStatements': IssueType.COMPLEXITY,
    'MagicNumber': IssueType.CODE_STYLE,
    'MandatoryBracesIfStatements': IssueType.CODE_STYLE,
    'MaxLineLength': IssueType.CODE_STYLE,
    'MayBeConst': IssueType.BEST_PRACTICES,
    'ModifierOrder': IssueType.CODE_STYLE,
    'NestedClassesVisibility': IssueType.BEST_PRACTICES,
    'NewLineAtEndOfFile': IssueType.CODE_STYLE,
    'NoTabs': IssueType.CODE_STYLE,
    'OptionalAbstractKeyword': IssueType.CODE_STYLE,
    'OptionalUnit': IssueType.CODE_STYLE,
    'OptionalWhenBraces': IssueType.CODE_STYLE,
    'PreferToOverPairSyntax': IssueType.BEST_PRACTICES,
    'ProtectedMemberInFinalClass': IssueType.BEST_PRACTICES,
    'RedundantExplicitType': IssueType.CODE_STYLE,
    'RedundantVisibilityModifierRule': IssueType.CODE_STYLE,
    'ReturnCount': IssueType.COMPLEXITY,
    'SafeCast': IssueType.BEST_PRACTICES,
    'SerialVersionUIDInSerializableClass': IssueType.BEST_PRACTICES,
    'SpacingBetweenPackageAndImports': IssueType.CODE_STYLE,
    'ThrowsCount': IssueType.COMPLEXITY,
    'TrailingWhitespace': IssueType.CODE_STYLE,
    'UnderscoresInNumericLiterals': IssueType.CODE_STYLE,
    'UnnecessaryAbstractClass': IssueType.BEST_PRACTICES,
    'UnnecessaryAnnotationUseSiteTarget': IssueType.BEST_PRACTICES,
    'UnnecessaryApply': IssueType.CODE_STYLE,
    'UnnecessaryInheritance': IssueType.BEST_PRACTICES,
    'UnnecessaryLet': IssueType.CODE_STYLE,
    'UnnecessaryParentheses': IssueType.CODE_STYLE,
    'UntilInsteadOfRangeTo': IssueType.BEST_PRACTICES,
    'UnusedImports': IssueType.BEST_PRACTICES,
    'UnusedPrivateClass': IssueType.BEST_PRACTICES,
    'UnusedPrivateMember': IssueType.BEST_PRACTICES,
    'UseArrayLiteralsInAnnotations': IssueType.CODE_STYLE,
    'UseCheckOrError': IssueType.BEST_PRACTICES,
    'UseDataClass': IssueType.BEST_PRACTICES,
    'UseIfInsteadOfWhen': IssueType.BEST_PRACTICES,
    'UseRequire': IssueType.BEST_PRACTICES,
    'UselessCallOnNotNull': IssueType.BEST_PRACTICES,
    'UtilityClassWithPublicConstructor': IssueType.BEST_PRACTICES,
    'VarCouldBeVal': IssueType.BEST_PRACTICES,
    'WildcardImport': IssueType.BEST_PRACTICES,
}
