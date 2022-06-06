###### Class me.inject.InjectTool (me.inject.InjectTool)
.class public Lme/inject/InjectTool;
.super Ljava/lang/Object;
.source "InjectTool.java"


# static fields
.field public static final TAG:Ljava/lang/String; = "InjectTool"


# direct methods
.method public constructor <init>()V
    .registers 1

    .line 5
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

#### invoke-static {v0}, Lme/inject/InjectTool;->e(Ljava/lang/String;)V
.method public static e(Ljava/lang/String;)V
    .registers 2
    .param p0, "msg"    # Ljava/lang/String;

    .line 8
    const-string v0, "InjectTool"

    invoke-static {v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    .line 9
    return-void
.end method

