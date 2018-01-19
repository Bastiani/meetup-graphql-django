import graphene
from graphene_django import DjangoObjectType

from posts.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()


class CreatePost(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    content = graphene.String()

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()

        return CreatePost(
            id=post.id,
            title=post.title,
            content=post.content,
        )


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
