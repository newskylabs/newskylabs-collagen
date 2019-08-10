# Experiments with Musical Notation

Collagen is a useful tool to augment digit datasets - but it can be
applied to other datasets as well. Let's experiment with a simple set
of musical notes and data augmentation.


## The *notes000* Dataset

The notes dataset consists out of 9 simple musical notes:

![collagen sequence 012345678 --dataset notes000](img/sequence.012345678.notes000.000.png "collagen sequence 012345678 --dataset notes000")

  - A whole note
  - A half note (stem pointing upwards)
  - A quarter note (up)
  - An eighth note (up)
  - A sixteenth note (up)
  - A half note (stem pointing downwards)
  - A quarter note (down)
  - An eighth note (down)
  - A sixteenth note (down)

The notes are encoded with the digits between 0 and 8 and therefore we
can use the same commands we used to visualize digits as well.  The
image above, for example, was generated with the command:

```python
collagen sequence 012345678 --dataset notes000
```

Let's see how we can use collagen to generate a set of images for deep
learning.

## Zoom

## Erosion

## Dilation

## Translation


